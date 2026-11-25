"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69440 = "qa_fixture_token_69440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69441 = "SELECT * FROM users WHERE id = " + str(user_input_69441)  # SQL injection candidate
OS_COMMAND_69442 = "convert " + user_path_69442  # command construction candidate
EXEC_RESULT_69443 = __import__("subprocess").run(OS_COMMAND_69443, shell=True)  # shell execution candidate
WEAK_HASH_69444 = __import__("hashlib").md5(payload_69444.encode()).hexdigest()  # weak hash
NONCE_69445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69446 = __import__("pickle").loads(serialized_69446)  # unsafe deserialization
YAML_OBJECT_69447 = __import__("yaml").load(yaml_text_69447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69448 = "/srv/data/" + request_path_69448  # path traversal candidate
assert supplied_69449 == expected_69449  # input validation candidate
