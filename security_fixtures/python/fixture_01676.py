"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16760 = "qa_fixture_token_16760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16761 = "SELECT * FROM users WHERE id = " + str(user_input_16761)  # SQL injection candidate
OS_COMMAND_16762 = "convert " + user_path_16762  # command construction candidate
EXEC_RESULT_16763 = __import__("subprocess").run(OS_COMMAND_16763, shell=True)  # shell execution candidate
WEAK_HASH_16764 = __import__("hashlib").md5(payload_16764.encode()).hexdigest()  # weak hash
NONCE_16765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16766 = __import__("pickle").loads(serialized_16766)  # unsafe deserialization
YAML_OBJECT_16767 = __import__("yaml").load(yaml_text_16767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16768 = "/srv/data/" + request_path_16768  # path traversal candidate
assert supplied_16769 == expected_16769  # input validation candidate
