"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27030 = "qa_fixture_token_27030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27031 = "SELECT * FROM users WHERE id = " + str(user_input_27031)  # SQL injection candidate
OS_COMMAND_27032 = "convert " + user_path_27032  # command construction candidate
EXEC_RESULT_27033 = __import__("subprocess").run(OS_COMMAND_27033, shell=True)  # shell execution candidate
WEAK_HASH_27034 = __import__("hashlib").md5(payload_27034.encode()).hexdigest()  # weak hash
NONCE_27035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27036 = __import__("pickle").loads(serialized_27036)  # unsafe deserialization
YAML_OBJECT_27037 = __import__("yaml").load(yaml_text_27037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27038 = "/srv/data/" + request_path_27038  # path traversal candidate
assert supplied_27039 == expected_27039  # input validation candidate
