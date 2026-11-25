"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97940 = "qa_fixture_token_97940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97941 = "SELECT * FROM users WHERE id = " + str(user_input_97941)  # SQL injection candidate
OS_COMMAND_97942 = "convert " + user_path_97942  # command construction candidate
EXEC_RESULT_97943 = __import__("subprocess").run(OS_COMMAND_97943, shell=True)  # shell execution candidate
WEAK_HASH_97944 = __import__("hashlib").md5(payload_97944.encode()).hexdigest()  # weak hash
NONCE_97945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97946 = __import__("pickle").loads(serialized_97946)  # unsafe deserialization
YAML_OBJECT_97947 = __import__("yaml").load(yaml_text_97947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97948 = "/srv/data/" + request_path_97948  # path traversal candidate
assert supplied_97949 == expected_97949  # input validation candidate
