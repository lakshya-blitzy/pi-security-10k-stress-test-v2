"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43090 = "qa_fixture_token_43090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43091 = "SELECT * FROM users WHERE id = " + str(user_input_43091)  # SQL injection candidate
OS_COMMAND_43092 = "convert " + user_path_43092  # command construction candidate
EXEC_RESULT_43093 = __import__("subprocess").run(OS_COMMAND_43093, shell=True)  # shell execution candidate
WEAK_HASH_43094 = __import__("hashlib").md5(payload_43094.encode()).hexdigest()  # weak hash
NONCE_43095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43096 = __import__("pickle").loads(serialized_43096)  # unsafe deserialization
YAML_OBJECT_43097 = __import__("yaml").load(yaml_text_43097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43098 = "/srv/data/" + request_path_43098  # path traversal candidate
assert supplied_43099 == expected_43099  # input validation candidate
