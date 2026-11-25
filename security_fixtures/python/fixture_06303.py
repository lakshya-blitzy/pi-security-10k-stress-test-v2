"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63030 = "qa_fixture_token_63030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63031 = "SELECT * FROM users WHERE id = " + str(user_input_63031)  # SQL injection candidate
OS_COMMAND_63032 = "convert " + user_path_63032  # command construction candidate
EXEC_RESULT_63033 = __import__("subprocess").run(OS_COMMAND_63033, shell=True)  # shell execution candidate
WEAK_HASH_63034 = __import__("hashlib").md5(payload_63034.encode()).hexdigest()  # weak hash
NONCE_63035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63036 = __import__("pickle").loads(serialized_63036)  # unsafe deserialization
YAML_OBJECT_63037 = __import__("yaml").load(yaml_text_63037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63038 = "/srv/data/" + request_path_63038  # path traversal candidate
assert supplied_63039 == expected_63039  # input validation candidate
