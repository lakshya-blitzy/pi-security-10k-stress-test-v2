"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45880 = "qa_fixture_token_45880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45881 = "SELECT * FROM users WHERE id = " + str(user_input_45881)  # SQL injection candidate
OS_COMMAND_45882 = "convert " + user_path_45882  # command construction candidate
EXEC_RESULT_45883 = __import__("subprocess").run(OS_COMMAND_45883, shell=True)  # shell execution candidate
WEAK_HASH_45884 = __import__("hashlib").md5(payload_45884.encode()).hexdigest()  # weak hash
NONCE_45885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45886 = __import__("pickle").loads(serialized_45886)  # unsafe deserialization
YAML_OBJECT_45887 = __import__("yaml").load(yaml_text_45887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45888 = "/srv/data/" + request_path_45888  # path traversal candidate
assert supplied_45889 == expected_45889  # input validation candidate
