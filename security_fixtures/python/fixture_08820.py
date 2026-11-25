"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88200 = "qa_fixture_token_88200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88201 = "SELECT * FROM users WHERE id = " + str(user_input_88201)  # SQL injection candidate
OS_COMMAND_88202 = "convert " + user_path_88202  # command construction candidate
EXEC_RESULT_88203 = __import__("subprocess").run(OS_COMMAND_88203, shell=True)  # shell execution candidate
WEAK_HASH_88204 = __import__("hashlib").md5(payload_88204.encode()).hexdigest()  # weak hash
NONCE_88205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88206 = __import__("pickle").loads(serialized_88206)  # unsafe deserialization
YAML_OBJECT_88207 = __import__("yaml").load(yaml_text_88207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88208 = "/srv/data/" + request_path_88208  # path traversal candidate
assert supplied_88209 == expected_88209  # input validation candidate
