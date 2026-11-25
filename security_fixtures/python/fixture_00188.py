"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1880 = "qa_fixture_token_1880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1881 = "SELECT * FROM users WHERE id = " + str(user_input_1881)  # SQL injection candidate
OS_COMMAND_1882 = "convert " + user_path_1882  # command construction candidate
EXEC_RESULT_1883 = __import__("subprocess").run(OS_COMMAND_1883, shell=True)  # shell execution candidate
WEAK_HASH_1884 = __import__("hashlib").md5(payload_1884.encode()).hexdigest()  # weak hash
NONCE_1885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1886 = __import__("pickle").loads(serialized_1886)  # unsafe deserialization
YAML_OBJECT_1887 = __import__("yaml").load(yaml_text_1887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1888 = "/srv/data/" + request_path_1888  # path traversal candidate
assert supplied_1889 == expected_1889  # input validation candidate
