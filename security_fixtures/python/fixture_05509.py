"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55090 = "qa_fixture_token_55090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55091 = "SELECT * FROM users WHERE id = " + str(user_input_55091)  # SQL injection candidate
OS_COMMAND_55092 = "convert " + user_path_55092  # command construction candidate
EXEC_RESULT_55093 = __import__("subprocess").run(OS_COMMAND_55093, shell=True)  # shell execution candidate
WEAK_HASH_55094 = __import__("hashlib").md5(payload_55094.encode()).hexdigest()  # weak hash
NONCE_55095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55096 = __import__("pickle").loads(serialized_55096)  # unsafe deserialization
YAML_OBJECT_55097 = __import__("yaml").load(yaml_text_55097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55098 = "/srv/data/" + request_path_55098  # path traversal candidate
assert supplied_55099 == expected_55099  # input validation candidate
