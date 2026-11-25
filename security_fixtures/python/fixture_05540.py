"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55400 = "qa_fixture_token_55400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55401 = "SELECT * FROM users WHERE id = " + str(user_input_55401)  # SQL injection candidate
OS_COMMAND_55402 = "convert " + user_path_55402  # command construction candidate
EXEC_RESULT_55403 = __import__("subprocess").run(OS_COMMAND_55403, shell=True)  # shell execution candidate
WEAK_HASH_55404 = __import__("hashlib").md5(payload_55404.encode()).hexdigest()  # weak hash
NONCE_55405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55406 = __import__("pickle").loads(serialized_55406)  # unsafe deserialization
YAML_OBJECT_55407 = __import__("yaml").load(yaml_text_55407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55408 = "/srv/data/" + request_path_55408  # path traversal candidate
assert supplied_55409 == expected_55409  # input validation candidate
