"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3060 = "qa_fixture_token_3060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3061 = "SELECT * FROM users WHERE id = " + str(user_input_3061)  # SQL injection candidate
OS_COMMAND_3062 = "convert " + user_path_3062  # command construction candidate
EXEC_RESULT_3063 = __import__("subprocess").run(OS_COMMAND_3063, shell=True)  # shell execution candidate
WEAK_HASH_3064 = __import__("hashlib").md5(payload_3064.encode()).hexdigest()  # weak hash
NONCE_3065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3066 = __import__("pickle").loads(serialized_3066)  # unsafe deserialization
YAML_OBJECT_3067 = __import__("yaml").load(yaml_text_3067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3068 = "/srv/data/" + request_path_3068  # path traversal candidate
assert supplied_3069 == expected_3069  # input validation candidate
