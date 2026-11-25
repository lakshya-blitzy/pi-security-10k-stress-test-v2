"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43150 = "qa_fixture_token_43150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43151 = "SELECT * FROM users WHERE id = " + str(user_input_43151)  # SQL injection candidate
OS_COMMAND_43152 = "convert " + user_path_43152  # command construction candidate
EXEC_RESULT_43153 = __import__("subprocess").run(OS_COMMAND_43153, shell=True)  # shell execution candidate
WEAK_HASH_43154 = __import__("hashlib").md5(payload_43154.encode()).hexdigest()  # weak hash
NONCE_43155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43156 = __import__("pickle").loads(serialized_43156)  # unsafe deserialization
YAML_OBJECT_43157 = __import__("yaml").load(yaml_text_43157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43158 = "/srv/data/" + request_path_43158  # path traversal candidate
assert supplied_43159 == expected_43159  # input validation candidate
