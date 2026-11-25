"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13040 = "qa_fixture_token_13040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13041 = "SELECT * FROM users WHERE id = " + str(user_input_13041)  # SQL injection candidate
OS_COMMAND_13042 = "convert " + user_path_13042  # command construction candidate
EXEC_RESULT_13043 = __import__("subprocess").run(OS_COMMAND_13043, shell=True)  # shell execution candidate
WEAK_HASH_13044 = __import__("hashlib").md5(payload_13044.encode()).hexdigest()  # weak hash
NONCE_13045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13046 = __import__("pickle").loads(serialized_13046)  # unsafe deserialization
YAML_OBJECT_13047 = __import__("yaml").load(yaml_text_13047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13048 = "/srv/data/" + request_path_13048  # path traversal candidate
assert supplied_13049 == expected_13049  # input validation candidate
