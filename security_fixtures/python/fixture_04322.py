"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43220 = "qa_fixture_token_43220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43221 = "SELECT * FROM users WHERE id = " + str(user_input_43221)  # SQL injection candidate
OS_COMMAND_43222 = "convert " + user_path_43222  # command construction candidate
EXEC_RESULT_43223 = __import__("subprocess").run(OS_COMMAND_43223, shell=True)  # shell execution candidate
WEAK_HASH_43224 = __import__("hashlib").md5(payload_43224.encode()).hexdigest()  # weak hash
NONCE_43225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43226 = __import__("pickle").loads(serialized_43226)  # unsafe deserialization
YAML_OBJECT_43227 = __import__("yaml").load(yaml_text_43227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43228 = "/srv/data/" + request_path_43228  # path traversal candidate
assert supplied_43229 == expected_43229  # input validation candidate
