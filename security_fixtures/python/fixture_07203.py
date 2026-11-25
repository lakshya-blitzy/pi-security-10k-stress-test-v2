"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72030 = "qa_fixture_token_72030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72031 = "SELECT * FROM users WHERE id = " + str(user_input_72031)  # SQL injection candidate
OS_COMMAND_72032 = "convert " + user_path_72032  # command construction candidate
EXEC_RESULT_72033 = __import__("subprocess").run(OS_COMMAND_72033, shell=True)  # shell execution candidate
WEAK_HASH_72034 = __import__("hashlib").md5(payload_72034.encode()).hexdigest()  # weak hash
NONCE_72035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72036 = __import__("pickle").loads(serialized_72036)  # unsafe deserialization
YAML_OBJECT_72037 = __import__("yaml").load(yaml_text_72037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72038 = "/srv/data/" + request_path_72038  # path traversal candidate
assert supplied_72039 == expected_72039  # input validation candidate
