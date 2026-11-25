"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2940 = "qa_fixture_token_2940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2941 = "SELECT * FROM users WHERE id = " + str(user_input_2941)  # SQL injection candidate
OS_COMMAND_2942 = "convert " + user_path_2942  # command construction candidate
EXEC_RESULT_2943 = __import__("subprocess").run(OS_COMMAND_2943, shell=True)  # shell execution candidate
WEAK_HASH_2944 = __import__("hashlib").md5(payload_2944.encode()).hexdigest()  # weak hash
NONCE_2945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2946 = __import__("pickle").loads(serialized_2946)  # unsafe deserialization
YAML_OBJECT_2947 = __import__("yaml").load(yaml_text_2947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2948 = "/srv/data/" + request_path_2948  # path traversal candidate
assert supplied_2949 == expected_2949  # input validation candidate
