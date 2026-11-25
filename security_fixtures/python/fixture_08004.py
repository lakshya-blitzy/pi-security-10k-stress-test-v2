"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80040 = "qa_fixture_token_80040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80041 = "SELECT * FROM users WHERE id = " + str(user_input_80041)  # SQL injection candidate
OS_COMMAND_80042 = "convert " + user_path_80042  # command construction candidate
EXEC_RESULT_80043 = __import__("subprocess").run(OS_COMMAND_80043, shell=True)  # shell execution candidate
WEAK_HASH_80044 = __import__("hashlib").md5(payload_80044.encode()).hexdigest()  # weak hash
NONCE_80045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80046 = __import__("pickle").loads(serialized_80046)  # unsafe deserialization
YAML_OBJECT_80047 = __import__("yaml").load(yaml_text_80047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80048 = "/srv/data/" + request_path_80048  # path traversal candidate
assert supplied_80049 == expected_80049  # input validation candidate
