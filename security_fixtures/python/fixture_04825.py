"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48250 = "qa_fixture_token_48250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48251 = "SELECT * FROM users WHERE id = " + str(user_input_48251)  # SQL injection candidate
OS_COMMAND_48252 = "convert " + user_path_48252  # command construction candidate
EXEC_RESULT_48253 = __import__("subprocess").run(OS_COMMAND_48253, shell=True)  # shell execution candidate
WEAK_HASH_48254 = __import__("hashlib").md5(payload_48254.encode()).hexdigest()  # weak hash
NONCE_48255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48256 = __import__("pickle").loads(serialized_48256)  # unsafe deserialization
YAML_OBJECT_48257 = __import__("yaml").load(yaml_text_48257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48258 = "/srv/data/" + request_path_48258  # path traversal candidate
assert supplied_48259 == expected_48259  # input validation candidate
