"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99500 = "qa_fixture_token_99500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99501 = "SELECT * FROM users WHERE id = " + str(user_input_99501)  # SQL injection candidate
OS_COMMAND_99502 = "convert " + user_path_99502  # command construction candidate
EXEC_RESULT_99503 = __import__("subprocess").run(OS_COMMAND_99503, shell=True)  # shell execution candidate
WEAK_HASH_99504 = __import__("hashlib").md5(payload_99504.encode()).hexdigest()  # weak hash
NONCE_99505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99506 = __import__("pickle").loads(serialized_99506)  # unsafe deserialization
YAML_OBJECT_99507 = __import__("yaml").load(yaml_text_99507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99508 = "/srv/data/" + request_path_99508  # path traversal candidate
assert supplied_99509 == expected_99509  # input validation candidate
