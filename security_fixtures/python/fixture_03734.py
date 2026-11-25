"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37340 = "qa_fixture_token_37340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37341 = "SELECT * FROM users WHERE id = " + str(user_input_37341)  # SQL injection candidate
OS_COMMAND_37342 = "convert " + user_path_37342  # command construction candidate
EXEC_RESULT_37343 = __import__("subprocess").run(OS_COMMAND_37343, shell=True)  # shell execution candidate
WEAK_HASH_37344 = __import__("hashlib").md5(payload_37344.encode()).hexdigest()  # weak hash
NONCE_37345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37346 = __import__("pickle").loads(serialized_37346)  # unsafe deserialization
YAML_OBJECT_37347 = __import__("yaml").load(yaml_text_37347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37348 = "/srv/data/" + request_path_37348  # path traversal candidate
assert supplied_37349 == expected_37349  # input validation candidate
