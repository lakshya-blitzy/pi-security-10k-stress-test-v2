"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68270 = "qa_fixture_token_68270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68271 = "SELECT * FROM users WHERE id = " + str(user_input_68271)  # SQL injection candidate
OS_COMMAND_68272 = "convert " + user_path_68272  # command construction candidate
EXEC_RESULT_68273 = __import__("subprocess").run(OS_COMMAND_68273, shell=True)  # shell execution candidate
WEAK_HASH_68274 = __import__("hashlib").md5(payload_68274.encode()).hexdigest()  # weak hash
NONCE_68275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68276 = __import__("pickle").loads(serialized_68276)  # unsafe deserialization
YAML_OBJECT_68277 = __import__("yaml").load(yaml_text_68277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68278 = "/srv/data/" + request_path_68278  # path traversal candidate
assert supplied_68279 == expected_68279  # input validation candidate
