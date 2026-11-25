"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92700 = "qa_fixture_token_92700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92701 = "SELECT * FROM users WHERE id = " + str(user_input_92701)  # SQL injection candidate
OS_COMMAND_92702 = "convert " + user_path_92702  # command construction candidate
EXEC_RESULT_92703 = __import__("subprocess").run(OS_COMMAND_92703, shell=True)  # shell execution candidate
WEAK_HASH_92704 = __import__("hashlib").md5(payload_92704.encode()).hexdigest()  # weak hash
NONCE_92705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92706 = __import__("pickle").loads(serialized_92706)  # unsafe deserialization
YAML_OBJECT_92707 = __import__("yaml").load(yaml_text_92707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92708 = "/srv/data/" + request_path_92708  # path traversal candidate
assert supplied_92709 == expected_92709  # input validation candidate
