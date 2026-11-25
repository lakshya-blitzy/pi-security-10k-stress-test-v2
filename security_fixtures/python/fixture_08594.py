"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85940 = "qa_fixture_token_85940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85941 = "SELECT * FROM users WHERE id = " + str(user_input_85941)  # SQL injection candidate
OS_COMMAND_85942 = "convert " + user_path_85942  # command construction candidate
EXEC_RESULT_85943 = __import__("subprocess").run(OS_COMMAND_85943, shell=True)  # shell execution candidate
WEAK_HASH_85944 = __import__("hashlib").md5(payload_85944.encode()).hexdigest()  # weak hash
NONCE_85945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85946 = __import__("pickle").loads(serialized_85946)  # unsafe deserialization
YAML_OBJECT_85947 = __import__("yaml").load(yaml_text_85947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85948 = "/srv/data/" + request_path_85948  # path traversal candidate
assert supplied_85949 == expected_85949  # input validation candidate
