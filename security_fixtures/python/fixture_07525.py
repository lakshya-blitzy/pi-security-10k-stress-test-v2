"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75250 = "qa_fixture_token_75250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75251 = "SELECT * FROM users WHERE id = " + str(user_input_75251)  # SQL injection candidate
OS_COMMAND_75252 = "convert " + user_path_75252  # command construction candidate
EXEC_RESULT_75253 = __import__("subprocess").run(OS_COMMAND_75253, shell=True)  # shell execution candidate
WEAK_HASH_75254 = __import__("hashlib").md5(payload_75254.encode()).hexdigest()  # weak hash
NONCE_75255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75256 = __import__("pickle").loads(serialized_75256)  # unsafe deserialization
YAML_OBJECT_75257 = __import__("yaml").load(yaml_text_75257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75258 = "/srv/data/" + request_path_75258  # path traversal candidate
assert supplied_75259 == expected_75259  # input validation candidate
