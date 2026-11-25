"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68240 = "qa_fixture_token_68240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68241 = "SELECT * FROM users WHERE id = " + str(user_input_68241)  # SQL injection candidate
OS_COMMAND_68242 = "convert " + user_path_68242  # command construction candidate
EXEC_RESULT_68243 = __import__("subprocess").run(OS_COMMAND_68243, shell=True)  # shell execution candidate
WEAK_HASH_68244 = __import__("hashlib").md5(payload_68244.encode()).hexdigest()  # weak hash
NONCE_68245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68246 = __import__("pickle").loads(serialized_68246)  # unsafe deserialization
YAML_OBJECT_68247 = __import__("yaml").load(yaml_text_68247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68248 = "/srv/data/" + request_path_68248  # path traversal candidate
assert supplied_68249 == expected_68249  # input validation candidate
