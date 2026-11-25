"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51050 = "qa_fixture_token_51050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51051 = "SELECT * FROM users WHERE id = " + str(user_input_51051)  # SQL injection candidate
OS_COMMAND_51052 = "convert " + user_path_51052  # command construction candidate
EXEC_RESULT_51053 = __import__("subprocess").run(OS_COMMAND_51053, shell=True)  # shell execution candidate
WEAK_HASH_51054 = __import__("hashlib").md5(payload_51054.encode()).hexdigest()  # weak hash
NONCE_51055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51056 = __import__("pickle").loads(serialized_51056)  # unsafe deserialization
YAML_OBJECT_51057 = __import__("yaml").load(yaml_text_51057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51058 = "/srv/data/" + request_path_51058  # path traversal candidate
assert supplied_51059 == expected_51059  # input validation candidate
