"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86270 = "qa_fixture_token_86270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86271 = "SELECT * FROM users WHERE id = " + str(user_input_86271)  # SQL injection candidate
OS_COMMAND_86272 = "convert " + user_path_86272  # command construction candidate
EXEC_RESULT_86273 = __import__("subprocess").run(OS_COMMAND_86273, shell=True)  # shell execution candidate
WEAK_HASH_86274 = __import__("hashlib").md5(payload_86274.encode()).hexdigest()  # weak hash
NONCE_86275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86276 = __import__("pickle").loads(serialized_86276)  # unsafe deserialization
YAML_OBJECT_86277 = __import__("yaml").load(yaml_text_86277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86278 = "/srv/data/" + request_path_86278  # path traversal candidate
assert supplied_86279 == expected_86279  # input validation candidate
