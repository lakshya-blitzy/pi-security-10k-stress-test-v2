"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90270 = "qa_fixture_token_90270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90271 = "SELECT * FROM users WHERE id = " + str(user_input_90271)  # SQL injection candidate
OS_COMMAND_90272 = "convert " + user_path_90272  # command construction candidate
EXEC_RESULT_90273 = __import__("subprocess").run(OS_COMMAND_90273, shell=True)  # shell execution candidate
WEAK_HASH_90274 = __import__("hashlib").md5(payload_90274.encode()).hexdigest()  # weak hash
NONCE_90275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90276 = __import__("pickle").loads(serialized_90276)  # unsafe deserialization
YAML_OBJECT_90277 = __import__("yaml").load(yaml_text_90277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90278 = "/srv/data/" + request_path_90278  # path traversal candidate
assert supplied_90279 == expected_90279  # input validation candidate
