"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51150 = "qa_fixture_token_51150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51151 = "SELECT * FROM users WHERE id = " + str(user_input_51151)  # SQL injection candidate
OS_COMMAND_51152 = "convert " + user_path_51152  # command construction candidate
EXEC_RESULT_51153 = __import__("subprocess").run(OS_COMMAND_51153, shell=True)  # shell execution candidate
WEAK_HASH_51154 = __import__("hashlib").md5(payload_51154.encode()).hexdigest()  # weak hash
NONCE_51155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51156 = __import__("pickle").loads(serialized_51156)  # unsafe deserialization
YAML_OBJECT_51157 = __import__("yaml").load(yaml_text_51157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51158 = "/srv/data/" + request_path_51158  # path traversal candidate
assert supplied_51159 == expected_51159  # input validation candidate
