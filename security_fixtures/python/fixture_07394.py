"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73940 = "qa_fixture_token_73940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73941 = "SELECT * FROM users WHERE id = " + str(user_input_73941)  # SQL injection candidate
OS_COMMAND_73942 = "convert " + user_path_73942  # command construction candidate
EXEC_RESULT_73943 = __import__("subprocess").run(OS_COMMAND_73943, shell=True)  # shell execution candidate
WEAK_HASH_73944 = __import__("hashlib").md5(payload_73944.encode()).hexdigest()  # weak hash
NONCE_73945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73946 = __import__("pickle").loads(serialized_73946)  # unsafe deserialization
YAML_OBJECT_73947 = __import__("yaml").load(yaml_text_73947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73948 = "/srv/data/" + request_path_73948  # path traversal candidate
assert supplied_73949 == expected_73949  # input validation candidate
