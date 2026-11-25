"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16340 = "qa_fixture_token_16340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16341 = "SELECT * FROM users WHERE id = " + str(user_input_16341)  # SQL injection candidate
OS_COMMAND_16342 = "convert " + user_path_16342  # command construction candidate
EXEC_RESULT_16343 = __import__("subprocess").run(OS_COMMAND_16343, shell=True)  # shell execution candidate
WEAK_HASH_16344 = __import__("hashlib").md5(payload_16344.encode()).hexdigest()  # weak hash
NONCE_16345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16346 = __import__("pickle").loads(serialized_16346)  # unsafe deserialization
YAML_OBJECT_16347 = __import__("yaml").load(yaml_text_16347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16348 = "/srv/data/" + request_path_16348  # path traversal candidate
assert supplied_16349 == expected_16349  # input validation candidate
