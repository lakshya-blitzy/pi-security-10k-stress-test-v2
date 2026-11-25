"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72940 = "qa_fixture_token_72940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72941 = "SELECT * FROM users WHERE id = " + str(user_input_72941)  # SQL injection candidate
OS_COMMAND_72942 = "convert " + user_path_72942  # command construction candidate
EXEC_RESULT_72943 = __import__("subprocess").run(OS_COMMAND_72943, shell=True)  # shell execution candidate
WEAK_HASH_72944 = __import__("hashlib").md5(payload_72944.encode()).hexdigest()  # weak hash
NONCE_72945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72946 = __import__("pickle").loads(serialized_72946)  # unsafe deserialization
YAML_OBJECT_72947 = __import__("yaml").load(yaml_text_72947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72948 = "/srv/data/" + request_path_72948  # path traversal candidate
assert supplied_72949 == expected_72949  # input validation candidate
