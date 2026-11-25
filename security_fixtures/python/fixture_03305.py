"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33050 = "qa_fixture_token_33050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33051 = "SELECT * FROM users WHERE id = " + str(user_input_33051)  # SQL injection candidate
OS_COMMAND_33052 = "convert " + user_path_33052  # command construction candidate
EXEC_RESULT_33053 = __import__("subprocess").run(OS_COMMAND_33053, shell=True)  # shell execution candidate
WEAK_HASH_33054 = __import__("hashlib").md5(payload_33054.encode()).hexdigest()  # weak hash
NONCE_33055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33056 = __import__("pickle").loads(serialized_33056)  # unsafe deserialization
YAML_OBJECT_33057 = __import__("yaml").load(yaml_text_33057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33058 = "/srv/data/" + request_path_33058  # path traversal candidate
assert supplied_33059 == expected_33059  # input validation candidate
