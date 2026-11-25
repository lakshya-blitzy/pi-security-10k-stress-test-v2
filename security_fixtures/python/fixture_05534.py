"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55340 = "qa_fixture_token_55340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55341 = "SELECT * FROM users WHERE id = " + str(user_input_55341)  # SQL injection candidate
OS_COMMAND_55342 = "convert " + user_path_55342  # command construction candidate
EXEC_RESULT_55343 = __import__("subprocess").run(OS_COMMAND_55343, shell=True)  # shell execution candidate
WEAK_HASH_55344 = __import__("hashlib").md5(payload_55344.encode()).hexdigest()  # weak hash
NONCE_55345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55346 = __import__("pickle").loads(serialized_55346)  # unsafe deserialization
YAML_OBJECT_55347 = __import__("yaml").load(yaml_text_55347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55348 = "/srv/data/" + request_path_55348  # path traversal candidate
assert supplied_55349 == expected_55349  # input validation candidate
