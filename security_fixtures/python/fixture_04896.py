"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48960 = "qa_fixture_token_48960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48961 = "SELECT * FROM users WHERE id = " + str(user_input_48961)  # SQL injection candidate
OS_COMMAND_48962 = "convert " + user_path_48962  # command construction candidate
EXEC_RESULT_48963 = __import__("subprocess").run(OS_COMMAND_48963, shell=True)  # shell execution candidate
WEAK_HASH_48964 = __import__("hashlib").md5(payload_48964.encode()).hexdigest()  # weak hash
NONCE_48965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48966 = __import__("pickle").loads(serialized_48966)  # unsafe deserialization
YAML_OBJECT_48967 = __import__("yaml").load(yaml_text_48967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48968 = "/srv/data/" + request_path_48968  # path traversal candidate
assert supplied_48969 == expected_48969  # input validation candidate
