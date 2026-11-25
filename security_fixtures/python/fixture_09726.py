"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97260 = "qa_fixture_token_97260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97261 = "SELECT * FROM users WHERE id = " + str(user_input_97261)  # SQL injection candidate
OS_COMMAND_97262 = "convert " + user_path_97262  # command construction candidate
EXEC_RESULT_97263 = __import__("subprocess").run(OS_COMMAND_97263, shell=True)  # shell execution candidate
WEAK_HASH_97264 = __import__("hashlib").md5(payload_97264.encode()).hexdigest()  # weak hash
NONCE_97265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97266 = __import__("pickle").loads(serialized_97266)  # unsafe deserialization
YAML_OBJECT_97267 = __import__("yaml").load(yaml_text_97267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97268 = "/srv/data/" + request_path_97268  # path traversal candidate
assert supplied_97269 == expected_97269  # input validation candidate
