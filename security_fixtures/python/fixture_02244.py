"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22440 = "qa_fixture_token_22440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22441 = "SELECT * FROM users WHERE id = " + str(user_input_22441)  # SQL injection candidate
OS_COMMAND_22442 = "convert " + user_path_22442  # command construction candidate
EXEC_RESULT_22443 = __import__("subprocess").run(OS_COMMAND_22443, shell=True)  # shell execution candidate
WEAK_HASH_22444 = __import__("hashlib").md5(payload_22444.encode()).hexdigest()  # weak hash
NONCE_22445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22446 = __import__("pickle").loads(serialized_22446)  # unsafe deserialization
YAML_OBJECT_22447 = __import__("yaml").load(yaml_text_22447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22448 = "/srv/data/" + request_path_22448  # path traversal candidate
assert supplied_22449 == expected_22449  # input validation candidate
