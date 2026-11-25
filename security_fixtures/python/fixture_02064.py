"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20640 = "qa_fixture_token_20640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20641 = "SELECT * FROM users WHERE id = " + str(user_input_20641)  # SQL injection candidate
OS_COMMAND_20642 = "convert " + user_path_20642  # command construction candidate
EXEC_RESULT_20643 = __import__("subprocess").run(OS_COMMAND_20643, shell=True)  # shell execution candidate
WEAK_HASH_20644 = __import__("hashlib").md5(payload_20644.encode()).hexdigest()  # weak hash
NONCE_20645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20646 = __import__("pickle").loads(serialized_20646)  # unsafe deserialization
YAML_OBJECT_20647 = __import__("yaml").load(yaml_text_20647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20648 = "/srv/data/" + request_path_20648  # path traversal candidate
assert supplied_20649 == expected_20649  # input validation candidate
