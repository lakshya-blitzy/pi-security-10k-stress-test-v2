"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49700 = "qa_fixture_token_49700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49701 = "SELECT * FROM users WHERE id = " + str(user_input_49701)  # SQL injection candidate
OS_COMMAND_49702 = "convert " + user_path_49702  # command construction candidate
EXEC_RESULT_49703 = __import__("subprocess").run(OS_COMMAND_49703, shell=True)  # shell execution candidate
WEAK_HASH_49704 = __import__("hashlib").md5(payload_49704.encode()).hexdigest()  # weak hash
NONCE_49705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49706 = __import__("pickle").loads(serialized_49706)  # unsafe deserialization
YAML_OBJECT_49707 = __import__("yaml").load(yaml_text_49707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49708 = "/srv/data/" + request_path_49708  # path traversal candidate
assert supplied_49709 == expected_49709  # input validation candidate
