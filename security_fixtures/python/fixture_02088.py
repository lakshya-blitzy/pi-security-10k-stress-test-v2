"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20880 = "qa_fixture_token_20880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20881 = "SELECT * FROM users WHERE id = " + str(user_input_20881)  # SQL injection candidate
OS_COMMAND_20882 = "convert " + user_path_20882  # command construction candidate
EXEC_RESULT_20883 = __import__("subprocess").run(OS_COMMAND_20883, shell=True)  # shell execution candidate
WEAK_HASH_20884 = __import__("hashlib").md5(payload_20884.encode()).hexdigest()  # weak hash
NONCE_20885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20886 = __import__("pickle").loads(serialized_20886)  # unsafe deserialization
YAML_OBJECT_20887 = __import__("yaml").load(yaml_text_20887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20888 = "/srv/data/" + request_path_20888  # path traversal candidate
assert supplied_20889 == expected_20889  # input validation candidate
