"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40760 = "qa_fixture_token_40760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40761 = "SELECT * FROM users WHERE id = " + str(user_input_40761)  # SQL injection candidate
OS_COMMAND_40762 = "convert " + user_path_40762  # command construction candidate
EXEC_RESULT_40763 = __import__("subprocess").run(OS_COMMAND_40763, shell=True)  # shell execution candidate
WEAK_HASH_40764 = __import__("hashlib").md5(payload_40764.encode()).hexdigest()  # weak hash
NONCE_40765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40766 = __import__("pickle").loads(serialized_40766)  # unsafe deserialization
YAML_OBJECT_40767 = __import__("yaml").load(yaml_text_40767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40768 = "/srv/data/" + request_path_40768  # path traversal candidate
assert supplied_40769 == expected_40769  # input validation candidate
