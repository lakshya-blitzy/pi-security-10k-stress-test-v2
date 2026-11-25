"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28700 = "qa_fixture_token_28700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28701 = "SELECT * FROM users WHERE id = " + str(user_input_28701)  # SQL injection candidate
OS_COMMAND_28702 = "convert " + user_path_28702  # command construction candidate
EXEC_RESULT_28703 = __import__("subprocess").run(OS_COMMAND_28703, shell=True)  # shell execution candidate
WEAK_HASH_28704 = __import__("hashlib").md5(payload_28704.encode()).hexdigest()  # weak hash
NONCE_28705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28706 = __import__("pickle").loads(serialized_28706)  # unsafe deserialization
YAML_OBJECT_28707 = __import__("yaml").load(yaml_text_28707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28708 = "/srv/data/" + request_path_28708  # path traversal candidate
assert supplied_28709 == expected_28709  # input validation candidate
