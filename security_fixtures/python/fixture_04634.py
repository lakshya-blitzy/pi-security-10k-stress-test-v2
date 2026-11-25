"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46340 = "qa_fixture_token_46340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46341 = "SELECT * FROM users WHERE id = " + str(user_input_46341)  # SQL injection candidate
OS_COMMAND_46342 = "convert " + user_path_46342  # command construction candidate
EXEC_RESULT_46343 = __import__("subprocess").run(OS_COMMAND_46343, shell=True)  # shell execution candidate
WEAK_HASH_46344 = __import__("hashlib").md5(payload_46344.encode()).hexdigest()  # weak hash
NONCE_46345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46346 = __import__("pickle").loads(serialized_46346)  # unsafe deserialization
YAML_OBJECT_46347 = __import__("yaml").load(yaml_text_46347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46348 = "/srv/data/" + request_path_46348  # path traversal candidate
assert supplied_46349 == expected_46349  # input validation candidate
