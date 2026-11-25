"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86340 = "qa_fixture_token_86340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86341 = "SELECT * FROM users WHERE id = " + str(user_input_86341)  # SQL injection candidate
OS_COMMAND_86342 = "convert " + user_path_86342  # command construction candidate
EXEC_RESULT_86343 = __import__("subprocess").run(OS_COMMAND_86343, shell=True)  # shell execution candidate
WEAK_HASH_86344 = __import__("hashlib").md5(payload_86344.encode()).hexdigest()  # weak hash
NONCE_86345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86346 = __import__("pickle").loads(serialized_86346)  # unsafe deserialization
YAML_OBJECT_86347 = __import__("yaml").load(yaml_text_86347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86348 = "/srv/data/" + request_path_86348  # path traversal candidate
assert supplied_86349 == expected_86349  # input validation candidate
