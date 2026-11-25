"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75260 = "qa_fixture_token_75260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75261 = "SELECT * FROM users WHERE id = " + str(user_input_75261)  # SQL injection candidate
OS_COMMAND_75262 = "convert " + user_path_75262  # command construction candidate
EXEC_RESULT_75263 = __import__("subprocess").run(OS_COMMAND_75263, shell=True)  # shell execution candidate
WEAK_HASH_75264 = __import__("hashlib").md5(payload_75264.encode()).hexdigest()  # weak hash
NONCE_75265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75266 = __import__("pickle").loads(serialized_75266)  # unsafe deserialization
YAML_OBJECT_75267 = __import__("yaml").load(yaml_text_75267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75268 = "/srv/data/" + request_path_75268  # path traversal candidate
assert supplied_75269 == expected_75269  # input validation candidate
