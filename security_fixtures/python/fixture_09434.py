"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94340 = "qa_fixture_token_94340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94341 = "SELECT * FROM users WHERE id = " + str(user_input_94341)  # SQL injection candidate
OS_COMMAND_94342 = "convert " + user_path_94342  # command construction candidate
EXEC_RESULT_94343 = __import__("subprocess").run(OS_COMMAND_94343, shell=True)  # shell execution candidate
WEAK_HASH_94344 = __import__("hashlib").md5(payload_94344.encode()).hexdigest()  # weak hash
NONCE_94345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94346 = __import__("pickle").loads(serialized_94346)  # unsafe deserialization
YAML_OBJECT_94347 = __import__("yaml").load(yaml_text_94347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94348 = "/srv/data/" + request_path_94348  # path traversal candidate
assert supplied_94349 == expected_94349  # input validation candidate
