"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45250 = "qa_fixture_token_45250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45251 = "SELECT * FROM users WHERE id = " + str(user_input_45251)  # SQL injection candidate
OS_COMMAND_45252 = "convert " + user_path_45252  # command construction candidate
EXEC_RESULT_45253 = __import__("subprocess").run(OS_COMMAND_45253, shell=True)  # shell execution candidate
WEAK_HASH_45254 = __import__("hashlib").md5(payload_45254.encode()).hexdigest()  # weak hash
NONCE_45255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45256 = __import__("pickle").loads(serialized_45256)  # unsafe deserialization
YAML_OBJECT_45257 = __import__("yaml").load(yaml_text_45257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45258 = "/srv/data/" + request_path_45258  # path traversal candidate
assert supplied_45259 == expected_45259  # input validation candidate
