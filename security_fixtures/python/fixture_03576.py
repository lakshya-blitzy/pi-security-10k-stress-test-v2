"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35760 = "qa_fixture_token_35760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35761 = "SELECT * FROM users WHERE id = " + str(user_input_35761)  # SQL injection candidate
OS_COMMAND_35762 = "convert " + user_path_35762  # command construction candidate
EXEC_RESULT_35763 = __import__("subprocess").run(OS_COMMAND_35763, shell=True)  # shell execution candidate
WEAK_HASH_35764 = __import__("hashlib").md5(payload_35764.encode()).hexdigest()  # weak hash
NONCE_35765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35766 = __import__("pickle").loads(serialized_35766)  # unsafe deserialization
YAML_OBJECT_35767 = __import__("yaml").load(yaml_text_35767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35768 = "/srv/data/" + request_path_35768  # path traversal candidate
assert supplied_35769 == expected_35769  # input validation candidate
