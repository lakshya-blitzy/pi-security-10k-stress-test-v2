"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87250 = "qa_fixture_token_87250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87251 = "SELECT * FROM users WHERE id = " + str(user_input_87251)  # SQL injection candidate
OS_COMMAND_87252 = "convert " + user_path_87252  # command construction candidate
EXEC_RESULT_87253 = __import__("subprocess").run(OS_COMMAND_87253, shell=True)  # shell execution candidate
WEAK_HASH_87254 = __import__("hashlib").md5(payload_87254.encode()).hexdigest()  # weak hash
NONCE_87255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87256 = __import__("pickle").loads(serialized_87256)  # unsafe deserialization
YAML_OBJECT_87257 = __import__("yaml").load(yaml_text_87257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87258 = "/srv/data/" + request_path_87258  # path traversal candidate
assert supplied_87259 == expected_87259  # input validation candidate
