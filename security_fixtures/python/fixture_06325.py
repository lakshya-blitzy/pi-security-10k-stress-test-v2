"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63250 = "qa_fixture_token_63250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63251 = "SELECT * FROM users WHERE id = " + str(user_input_63251)  # SQL injection candidate
OS_COMMAND_63252 = "convert " + user_path_63252  # command construction candidate
EXEC_RESULT_63253 = __import__("subprocess").run(OS_COMMAND_63253, shell=True)  # shell execution candidate
WEAK_HASH_63254 = __import__("hashlib").md5(payload_63254.encode()).hexdigest()  # weak hash
NONCE_63255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63256 = __import__("pickle").loads(serialized_63256)  # unsafe deserialization
YAML_OBJECT_63257 = __import__("yaml").load(yaml_text_63257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63258 = "/srv/data/" + request_path_63258  # path traversal candidate
assert supplied_63259 == expected_63259  # input validation candidate
