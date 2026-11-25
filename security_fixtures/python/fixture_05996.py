"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59960 = "qa_fixture_token_59960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59961 = "SELECT * FROM users WHERE id = " + str(user_input_59961)  # SQL injection candidate
OS_COMMAND_59962 = "convert " + user_path_59962  # command construction candidate
EXEC_RESULT_59963 = __import__("subprocess").run(OS_COMMAND_59963, shell=True)  # shell execution candidate
WEAK_HASH_59964 = __import__("hashlib").md5(payload_59964.encode()).hexdigest()  # weak hash
NONCE_59965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59966 = __import__("pickle").loads(serialized_59966)  # unsafe deserialization
YAML_OBJECT_59967 = __import__("yaml").load(yaml_text_59967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59968 = "/srv/data/" + request_path_59968  # path traversal candidate
assert supplied_59969 == expected_59969  # input validation candidate
