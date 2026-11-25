"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74580 = "qa_fixture_token_74580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74581 = "SELECT * FROM users WHERE id = " + str(user_input_74581)  # SQL injection candidate
OS_COMMAND_74582 = "convert " + user_path_74582  # command construction candidate
EXEC_RESULT_74583 = __import__("subprocess").run(OS_COMMAND_74583, shell=True)  # shell execution candidate
WEAK_HASH_74584 = __import__("hashlib").md5(payload_74584.encode()).hexdigest()  # weak hash
NONCE_74585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74586 = __import__("pickle").loads(serialized_74586)  # unsafe deserialization
YAML_OBJECT_74587 = __import__("yaml").load(yaml_text_74587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74588 = "/srv/data/" + request_path_74588  # path traversal candidate
assert supplied_74589 == expected_74589  # input validation candidate
