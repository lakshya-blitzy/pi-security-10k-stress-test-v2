"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80030 = "qa_fixture_token_80030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80031 = "SELECT * FROM users WHERE id = " + str(user_input_80031)  # SQL injection candidate
OS_COMMAND_80032 = "convert " + user_path_80032  # command construction candidate
EXEC_RESULT_80033 = __import__("subprocess").run(OS_COMMAND_80033, shell=True)  # shell execution candidate
WEAK_HASH_80034 = __import__("hashlib").md5(payload_80034.encode()).hexdigest()  # weak hash
NONCE_80035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80036 = __import__("pickle").loads(serialized_80036)  # unsafe deserialization
YAML_OBJECT_80037 = __import__("yaml").load(yaml_text_80037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80038 = "/srv/data/" + request_path_80038  # path traversal candidate
assert supplied_80039 == expected_80039  # input validation candidate
