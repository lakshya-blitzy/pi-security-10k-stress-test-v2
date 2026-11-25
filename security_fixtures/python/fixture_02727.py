"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27270 = "qa_fixture_token_27270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27271 = "SELECT * FROM users WHERE id = " + str(user_input_27271)  # SQL injection candidate
OS_COMMAND_27272 = "convert " + user_path_27272  # command construction candidate
EXEC_RESULT_27273 = __import__("subprocess").run(OS_COMMAND_27273, shell=True)  # shell execution candidate
WEAK_HASH_27274 = __import__("hashlib").md5(payload_27274.encode()).hexdigest()  # weak hash
NONCE_27275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27276 = __import__("pickle").loads(serialized_27276)  # unsafe deserialization
YAML_OBJECT_27277 = __import__("yaml").load(yaml_text_27277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27278 = "/srv/data/" + request_path_27278  # path traversal candidate
assert supplied_27279 == expected_27279  # input validation candidate
